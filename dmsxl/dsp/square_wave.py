"""
1 Hz Square Wave Visualization (fs = 1 kHz)
- Figure 1:
  - Time-domain plot
  - Frequency-domain (FFT) magnitude plot (symmetric)
  - Zoomed-in frequency-domain plot (-10 Hz ~ 10 Hz)
- Figure 2:
  - Time-domain: original vs. re-sampled stems (aliasing demo)
  - Frequency-domain: spectrum of the re-sampled sequence (symmetric, ±100 Hz)
"""

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------
# Figure 1: Your original setup
# ---------------------------

# Sampling configuration (base reference)
fs = 1_000           # Sampling frequency in Hz (1 kHz)
t_end = 10            # Duration in seconds
t = np.linspace(0, t_end, int(fs * t_end), endpoint=False)

# Generate 1 Hz square wave (shifted to 0–2 range)
f_square = 1         # Frequency of square wave (Hz)
square_wave = np.sign(np.sin(2 * np.pi * f_square * t)) + 1

# Compute FFT
n = len(square_wave)
freqs = np.fft.fftfreq(n, 1 / fs)
fft_values = np.fft.fft(square_wave)
fft_magnitude = np.abs(fft_values) / n

# Shift FFT for symmetric display
freqs_shifted = np.fft.fftshift(freqs)
fft_shifted = np.fft.fftshift(fft_magnitude)

# Theoretical sinc envelope (50% duty → pulse width = 0.5 s)
T_pulse = 0.5
sinc_envelope = np.abs(np.sinc(T_pulse * freqs_shifted))
sinc_envelope *= np.max(fft_shifted) if np.max(fft_shifted) > 0 else 1.0

# --- Plotting: Figure 1 ---
plt.figure(figsize=(10, 9))

# (1) Time-domain plot
plt.subplot(3, 1, 1)
# For fs=1 kHz and t_end=2 s you have 2000 samples → show a reasonable window
plt.plot(t, square_wave, 'b')
plt.title("1 Hz Square Wave - Time Domain")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)

# (2) Full Frequency-domain plot (symmetric)
plt.subplot(3, 1, 2)
plt.plot(freqs_shifted, fft_shifted, 'r', label="FFT Magnitude")
plt.plot(freqs_shifted, sinc_envelope, 'k--', linewidth=1.5, label="sinc(f) Envelope")
plt.title("1 Hz Square Wave - Frequency Domain (Full Spectrum)")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.xlim(-100, 100)
plt.grid(True)
plt.legend()

# (3) Zoomed Frequency-domain plot (-10 Hz ~ 10 Hz)
plt.subplot(3, 1, 3)
plt.plot(freqs_shifted, fft_shifted, 'r', label="FFT Magnitude")
plt.plot(freqs_shifted, sinc_envelope, 'k--', linewidth=1.5, label="sinc(f) Envelope")
plt.title("1 Hz Square Wave - Frequency Domain (Zoomed: -10 Hz ~ 10 Hz)")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.xlim(-10, 10)
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

# ---------------------------
# Figure 2: Aliasing + Reconstruction demo
# ---------------------------

def zoh_reconstruct(t_grid: np.ndarray,
                    t_s: np.ndarray,
                    x_s: np.ndarray) -> np.ndarray:
    """
    Zero-Order Hold (rectangular hold).
    For each interval [t_s[k], t_s[k+1]), hold x_s[k] constant.
    """
    # Indices of the last sample not greater than each t
    idx = np.searchsorted(t_s, t_grid, side='right') - 1
    idx[idx < 0] = 0
    idx[idx >= len(x_s)] = len(x_s) - 1
    return x_s[idx]


def linear_reconstruct(t_grid: np.ndarray,
                       t_s: np.ndarray,
                       x_s: np.ndarray) -> np.ndarray:
    """
    Linear interpolation between adjacent samples.
    Outside the sampled range, hold endpoints.
    """
    return np.interp(t_grid, t_s, x_s, left=x_s[0], right=x_s[-1])


def sinc_reconstruct(t_grid: np.ndarray,
                     t_s: np.ndarray,
                     x_s: np.ndarray,
                     fs_target: float,
                     L: int = 20) -> np.ndarray:
    """
    Ideal bandlimited (Whittaker–Shannon) interpolation with
    truncated sinc kernel. L controls half-length of the kernel
    in samples (use larger L for better accuracy, slower speed).

    NOTE: Assumes signal is bandlimited within fs_target/2. If
          aliasing happened at sampling, sinc cannot restore it.
    """
    T = 1.0 / fs_target  # nominal sampling period used in the sinc argument
    y = np.zeros_like(t_grid)
    # For speed, restrict to nearby taps per grid point
    for k, tk in enumerate(t_s):
        # keep only t within [tk - L*T, tk + L*T]
        mask = (t_grid >= tk - L * T) & (t_grid <= tk + L * T)
        tau = (t_grid[mask] - tk) / T
        y[mask] += x_s[k] * np.sinc(tau)
    return y

# ===== Helpers for theoretical replicated spectrum =====
def next_pow2(n: int, min_factor: int = 1) -> int:
    n_fft = 1
    target = max(1, int(min_factor * n))
    while n_fft < target:
        n_fft <<= 1
    return n_fft

def fft_mag_hz(x: np.ndarray, fs: float, pad_factor: int = 8) -> tuple[np.ndarray, np.ndarray]:
    """
    Return (freq_axis_Hz, |FFT|/N) for sequence x sampled at fs (Hz).
    Uses zero-padding by pad_factor for a denser frequency grid.
    """
    n = len(x)
    n_fft = next_pow2(n, pad_factor)
    freq = np.fft.fftfreq(n_fft, d=1.0 / fs)
    X = np.fft.fft(x, n=n_fft) / n  # simple amplitude normalization
    return np.fft.fftshift(freq), np.fft.fftshift(np.abs(X))

def _make_linear_lookup(x_axis: np.ndarray, y_axis: np.ndarray):
    """
    Lightweight linear interpolator on a uniform x_axis. Out-of-range -> 0.0.
    """
    fmin = float(x_axis[0])
    fmax = float(x_axis[-1])
    df = float(x_axis[1] - x_axis[0])

    def lookup(q: np.ndarray) -> np.ndarray:
        idx = (q - fmin) / df
        i0 = np.floor(idx).astype(int)
        w = idx - i0
        valid = (i0 >= 0) & (i0 < len(x_axis) - 1)
        out = np.zeros_like(q, dtype=float)
        out[valid] = ((1.0 - w[valid]) * y_axis[i0[valid]]
                      + w[valid] * y_axis[i0[valid] + 1])
        return out

    return lookup

def replicated_spectrum(freq_axis: np.ndarray,
                        Xc_mag_axis: np.ndarray,
                        fs_sample: float,
                        replicas: int = 6) -> np.ndarray:
    """
    Approximate Σ_{k=-replicas..replicas} Xc(f - k*fs_sample), scaled by 1/T.
    This is the continuous-time replication model Xs(f) = (1/T) Σ_k Xc(f - k fs).
    """
    lookup = _make_linear_lookup(freq_axis, Xc_mag_axis)
    T = 1.0 / fs_sample
    acc = np.zeros_like(freq_axis, dtype=float)
    for k in range(-replicas, replicas + 1):
        acc += lookup(freq_axis - k * fs_sample)
    return acc * (1.0 / T)

# ---- Precompute a high-rate "continuous-time proxy" once (global cache) ----
# 20 kHz over 20 s gives a very sharp reference in frequency.
_fs_ref = 20_000.0
_t_end_ref = 20.0
_f0_ref = 1.0  # 1 Hz square
_t_ref = np.linspace(0.0, _t_end_ref, int(_fs_ref * _t_end_ref), endpoint=False)
_x_ref = np.sign(np.sin(2 * np.pi * _f0_ref * _t_ref)) + 1.0
_F_REF, _XC_MAG = fft_mag_hz(_x_ref, fs=_fs_ref, pad_factor=2)


def plot_figure2_for_fs(fs_sample: float,
                        show_time_window: tuple[float, float] = (0, 3),
                        show_recon_window: tuple[float, float] = (0, 2),
                        fft_xlim: tuple[float, float] = (-100, 100),
                        sinc_L: int = 30) -> None:
    """
    Make Figure 2 for a given sampling rate:
      1) Original vs. sample stems (time domain)
      2) Spectrum of sampled sequence (symmetric, ±100 Hz)
      3) Reconstructions (sinc / ZOH / linear) over a short window
    """
    # Sample the original (consider the original discrete series as "continuous" reference)
    Ts = 1.0 / fs_sample
    t_s = np.arange(0, t_end, Ts)
    # Use reference "continuous" signal by re-evaluating the known formula at t_s
    x_s = np.sign(np.sin(2 * np.pi * f_square * t_s)) + 1

    # ----- Figure 2 -----
    plt.figure(figsize=(10, 10))
    plt.suptitle(f"Figure 2 — Aliasing & Reconstruction at fs = {fs_sample:.3f} Hz")

    # (1) Time-domain: original vs. sampled stems (full window or trimmed)
    ax1 = plt.subplot(5, 1, 1)
    # Time window for clarity
    t0, t1 = show_time_window
    mask = (t >= t0) & (t <= t1)
    plt.plot(t[mask], square_wave[mask], label="Original (fs=1 kHz)")
    # Stems: show discrete samples
    # For plotting stems within the window
    s_mask = (t_s >= t0) & (t_s <= t1)
    plt.stem(t_s[s_mask], x_s[s_mask],
             linefmt='C1-', markerfmt='C1o', basefmt=' ',
             label=f"Samples (fs={fs_sample:g} Hz)")

    plt.title("Time Domain: Original vs. Sampled Stems")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    # (2) Frequency-domain: THEORETICAL replicated continuous-time spectrum in Hz
    #    Xs(f) = (1/T) * sum_k Xc(f - k*fs_sample)
    X_rep = replicated_spectrum(_F_REF, _XC_MAG, fs_sample=fs_sample, replicas=6)

    ax2 = plt.subplot(5, 1, 2)
    # Limit to same viewing window you already use via fft_xlim
    view_mask = (_F_REF >= fft_xlim[0]) & (_F_REF <= fft_xlim[1])
    plt.plot(_F_REF[view_mask], X_rep[view_mask])
    plt.title("Frequency Domain: Theoretical Replicated Spectrum  Σ Xc(f - k·fs)")
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Magnitude (scaled by 1/T)")
    plt.xlim(*fft_xlim)
    plt.grid(True)

    # (3) Reconstructions split into three panels: sinc, ZOH, linear (red solid lines)
    r0, r1 = show_recon_window
    r_mask = (t >= r0) & (t <= r1)
    s_mask_r = (t_s >= r0) & (t_s <= r1)

    # Reconstruct on the same dense grid t (from Figure 1)
    t_win = t[r_mask]
    x_ref_win = square_wave[r_mask]
    x_rec_sinc = sinc_reconstruct(t_win, t_s, x_s, fs_target=fs_sample, L=sinc_L)
    x_rec_zoh  = zoh_reconstruct(t_win, t_s, x_s)
    x_rec_lin  = linear_reconstruct(t_win, t_s, x_s)

    # --- (5,1,3): Sinc vs Original ---
    ax3 = plt.subplot(5, 1, 3)
    plt.plot(t_win, x_ref_win, label="Original (reference)", linewidth=1.5)
    plt.plot(t_win, x_rec_sinc, 'r-', linewidth=1.5, label=f"Sinc (L={sinc_L})")
    plt.stem(t_s[s_mask_r], x_s[s_mask_r], linefmt='C3-', markerfmt='C3o', basefmt=' ')
    plt.title("Reconstruction (Time Domain): Sinc vs Original")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()

    # --- (5,1,4): ZOH vs Original ---
    ax4 = plt.subplot(5, 1, 4)
    plt.plot(t_win, x_ref_win, label="Original (reference)", linewidth=1.5)
    plt.plot(t_win, x_rec_zoh, 'r-', linewidth=1.5, label="ZOH (rectangular hold)")
    plt.stem(t_s[s_mask_r], x_s[s_mask_r], linefmt='C3-', markerfmt='C3o', basefmt=' ')
    plt.title("Reconstruction (Time Domain): ZOH vs Original")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()

    # --- (5,1,5): Linear vs Original ---
    ax5 = plt.subplot(5, 1, 5)
    plt.plot(t_win, x_ref_win, label="Original (reference)", linewidth=1.5)
    plt.plot(t_win, x_rec_lin, 'r-', linewidth=1.5, label="Linear")
    plt.stem(t_s[s_mask_r], x_s[s_mask_r], linefmt='C3-', markerfmt='C3o', basefmt=' ')
    plt.title("Reconstruction (Time Domain): Linear vs Original")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()


# ---- Choose sample rates to demonstrate aliasing / fidelity tradeoffs ----
# Tips:
#   - Well above Nyquist (e.g., 50 Hz) shows good reconstructions.
#   - Near Nyquist (e.g., 3 Hz for a 1 Hz square's strong harmonics) shows distortion.
#   - Very low (e.g., 1.5 Hz) shows heavy aliasing.
fs_list = [50.0, 3.0, 0.9]

# Render Figure 2 for each chosen sample rate
for fs2 in fs_list:
    plot_figure2_for_fs(
        fs_sample=fs2,
        show_time_window=(0, 20),      # stems overlay window
        show_recon_window=(0, 20),     # reconstruction overlay window
        fft_xlim=(-100, 100),         # symmetric spectrum view
        sinc_L=30                     # sinc half-length (taps per side)
    )

