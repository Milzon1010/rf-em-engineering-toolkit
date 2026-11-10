import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def process_microwave_pm_log(file_path):
    print(f"Membaca file log NMS: {file_path}...")
    
    # 1. Load data CSV log NMS (asumsi kolom: Timestamp, Link_ID, RSL_dBm, Throughput_Mbps, Modulation)
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print("File tidak ditemukan. Pastikan path file sudah benar.")
        return

    # Konversi kolom waktu ke datetime
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    
    # Sort data berdasarkan waktu
    df = df.sort_values('Timestamp')

    # 2. Analisis Statistik Dasar
    print("\n--- RINGKASAN PERFORMA LINK MICROWAVE ---")
    print(f"Rata-rata RSL (Received Signal Level): {df['RSL_dBm'].mean():.2f} dBm")
    print(f"Rata-rata Throughput: {df['Throughput_Mbps'].mean():.2f} Mbps")
    print(f"RSL Terendah (Potensi Fading/Gangguan): {df['RSL_dBm'].min():.2f} dBm")

    # 3. Deteksi Anomali / Ambang Batas Kritis (Contoh: RSL di bawah -65 dBm)
    threshold_rsl = -65.0
    anomalies = df[df['RSL_dBm'] < threshold_rsl]
    print(f"Jumlah anomali (RSL < {threshold_rsl} dBm): {len(anomalies)} kejadian")

    # 4. Visualisasi Grafik Tren RSL dan Throughput
    plt.figure(figsize=(12, 8))

    # Grafik RSL
    plt.subplot(2, 1, 1)
    plt.plot(df['Timestamp'], df['RSL_dBm'], color='b', label='RSL (dBm)', linewidth=1.2)
    plt.axhline(y=threshold_rsl, color='r', linestyle='--', label=f'Threshold Min ({threshold_rsl} dBm)')
    plt.ylabel('RSL (dBm)')
    plt.title('Analisis Otomatis Log PM NMS Microwave Link')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(loc='lower left')

    # Grafik Throughput
    plt.subplot(2, 1, 2)
    plt.plot(df['Timestamp'], df['Throughput_Mbps'], color='g', label='Throughput (Mbps)', linewidth=1.2)
    plt.xlabel('Waktu (Timestamp)')
    plt.ylabel('Throughput (Mbps)')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(loc='lower left')

    plt.tight_layout()
    
    # Simpan hasil grafik ke file gambar
    output_image = 'nms_pm_analysis_report.png'
    plt.savefig(output_image)
    print(f"\nGrafik laporan berhasil disimpan ke '{output_image}'")
    
    # Tampilkan grafik
    plt.show()

# Contoh eksekusi fungsi (ganti 'sample_nms_log.csv' dengan file log kamu)
if __name__ == "__main__":
    # process_microwave_pm_log('sample_nms_log.csv')
    print("Skrip siap digunakan! Masukkan file CSV log NMS kamu ke fungsi di atas.")