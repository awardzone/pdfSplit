import os
import sys
import argparse
from pypdf import PdfReader, PdfWriter

def split_pdf(input_path, pages_per_split):
    # Controllo se il file di input esiste
    if not os.path.exists(input_path):
        print(f"Errore: Il file '{input_path}' non esiste.")
        sys.exit(1)

    # Creazione della cartella di output se non esiste
    output_dir = "out"
    os.makedirs(output_dir, exist_ok=True)

    try:
        # Lettura del PDF
        reader = PdfReader(input_path)
        total_pages = len(reader.pages)
        print(f"Il documento originale contiene {total_pages} pagine.")
    except Exception as e:
        print(f"Errore durante l'apertura del PDF: {e}")
        sys.exit(1)

    # Estrapolo il nome del file originale senza l'estensione
    base_name = os.path.splitext(os.path.basename(input_path))[0]

    part_num = 1
    
    # Ciclo attraverso le pagine del documento saltando di 'pages_per_split' alla volta
    for start_index in range(0, total_pages, pages_per_split):
        writer = PdfWriter()
        
        # Calcolo l'indice finale di questo blocco (gestisce automaticamente l'ultimo blocco più corto)
        end_index = min(start_index + pages_per_split, total_pages)
        
        # Aggiungo le pagine al nuovo file
        for page_num in range(start_index, end_index):
            writer.add_page(reader.pages[page_num])
            
        # Genero il nome del file con progressione numerica (es: documento_part_1.pdf)
        output_filename = os.path.join(output_dir, f"{base_name}_part_{part_num}.pdf")
        
        # Salvo il nuovo file PDF
        with open(output_filename, "wb") as output_file:
            writer.write(output_file)
            
        print(f"Salvato: {output_filename} (Pagine {start_index + 1} - {end_index})")
        
        part_num += 1

    print("\nSuddivisione completata con successo! I file si trovano nella cartella 'out/'.")

if __name__ == "__main__":
    # Configurazione dei parametri da riga di comando
    parser = argparse.ArgumentParser(description="Suddivide un file PDF in file più piccoli.")
    parser.add_argument("input_file", help="Il percorso del file PDF da suddividere")
    parser.add_argument("pages", type=int, help="Il numero di pagine per ogni file generato")
    
    args = parser.parse_args()
    
    if args.pages <= 0:
        print("Errore: Il numero di pagine deve essere maggiore di zero.")
        sys.exit(1)
        
    split_pdf(args.input_file, args.pages)
