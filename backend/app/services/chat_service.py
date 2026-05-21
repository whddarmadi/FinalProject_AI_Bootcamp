def get_response(text):

    text = text.lower()

    if "greeting" in text:
        return  """
SOP pelayanan:
1. Menerima pesanan
2. Input pesanan
3. Pembayaran
4. Pembuatan produk
5. Penyerahan produk
6. Membersihkan alat
"""
            
    elif "bonus" in text:
        return """
Bonus berdasarkan omset outlet:
50–59 juta → 0.5%
60–69 juta → 1%
70+ juta → 2%
"""


    elif "terlambat" in text:
        return """
Keterlambatan:
- Mengurangi 1/3 bonus
- Berulang bisa kena PHK
"""

    elif "seragam" in text:
        return """
Senin-Selasa: bebas berkerah
Rabu-Kamis: seragam Mbok Darmi
Jumat: batik
Sabtu-Minggu: seragam
"""

    return "Maaf, SOP belum tersedia."
