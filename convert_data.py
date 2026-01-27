import pandas as pd
import json

df = pd.read_excel('data produk.xlsx')
df['varian'] = df['varian'].where(pd.notna(df['varian']), None)

products = []
for _, row in df.iterrows():
    products.append({
        'nama': str(row['nama']).strip(),
        'varian': str(row['varian']).strip() if row['varian'] else None,
        'kategori': str(row['kategori']).strip()
    })

# Create JavaScript file content
js_content = """// ============================================================
// DATA PRODUK - KATALOG TOKO
// ============================================================
// File ini berisi semua data produk yang ditampilkan di website
// 
// CARA MENAMBAH PRODUK BARU:
// 1. Scroll ke bagian bawah array 'productsData'
// 2. Tambahkan objek baru dengan format:
//    { nama: "Nama Produk", varian: "Nama Varian", kategori: "Kategori" }
//    
//    - Jika produk TIDAK punya varian, gunakan: varian: null
//    - Jika produk PUNYA varian, buat beberapa baris dengan nama sama
//
// CONTOH:
// Produk tanpa varian:
//    { nama: "Sabun Mandi ABC", varian: null, kategori: "Sabun" },
//
// Produk dengan varian:
//    { nama: "Parfum XYZ", varian: "50ml", kategori: "Parfum" },
//    { nama: "Parfum XYZ", varian: "100ml", kategori: "Parfum" },
//
// KATEGORI YANG TERSEDIA:
// Kosmetik, Parfum, Baterai, Alat, Sabun, Obat Nyamuk, 
// Baby Care, Alat Kebersihan, Minyak Rambut, Deodorant, Shampoo, Odol
// (Anda juga bisa menambah kategori baru)
// ============================================================

const productsData = """

js_content += json.dumps(products, ensure_ascii=False, indent=2)
js_content += ';'

with open('products.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print('products.js created successfully!')
print(f'Total products: {len(products)}')
