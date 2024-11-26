Isti Zahra Eka Putri Katili_F55123090
# analisis best case sorting
1. Naive Method (Bubble Sort)
Best Case
- Input: Data sudah dalam urutan ascending (misalnya, [1, 2, 3, 4, 5]).
- Alasan: Pada Bubble Sort, jika data sudah terurut, algoritma hanya perlu melakukan satu iterasi penuh tanpa pertukaran elemen.
- Optimisasi: Dalam implementasi optimal, Bubble Sort dapat mendeteksi bahwa tidak ada elemen yang perlu ditukar, sehingga iterasi berikutnya dihentikan.
  
Kompleksitas
- Waktu O(n): Dalam best case, hanya dilakukan satu iterasi (n perbandingan, tanpa pertukaran elemen).
- Ruang O(1): Sorting dilakukan secara in-place, tanpa alokasi memori tambahan.
  
Proses Analisis
- Contoh input: [1, 2, 3, 4, 5].
- Iterasi 1: Bandingkan elemen bersebelahan (tidak ada swap, sorting selesai).

2. Conquer Method (Merge Sort)
Best Case
- Input: Merge Sort tidak memiliki perubahan besar dalam performa berdasarkan urutan input data karena strukturnya tetap membagi array menjadi dua dan menggabungkan kembali, apa pun kondisinya.
- Alasan: Bahkan dalam kasus terbaik (data sudah terurut), Merge Sort tetap membagi array hingga elemen individual sebelum menggabungkannya kembali.

Kompleksitas
- Waktu O(n log n): Terjadi pembagian array hingga mencapai elemen tunggal (log n), dan setiap tingkat pembagian membutuhkan O(n) waktu untuk penggabungan.
- Ruang O(n): Karena Merge Sort membutuhkan array tambahan untuk menyimpan hasil penggabungan.

Proses Analisis
- Contoh input: [1, 2, 3, 4, 5].
- Proses Pembagian: Dibagi menjadi [1, 2, 3] dan [4, 5], lalu terus dibagi hingga elemen tunggal.
- Penggabungan: Gabungkan [1] dan [2] menjadi [1, 2], lalu [1, 2] dengan [3] menjadi [1, 2, 3], dan seterusnya.

