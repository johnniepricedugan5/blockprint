import hashlib
import qrcode
import argparse
import pyfiglet


def hash_data(data: str, algo: str = 'sha256') -> str:
    """Возвращает хеш строки с использованием выбранного алгоритма."""
    h = hashlib.new(algo)
    h.update(data.encode('utf-8'))
    return h.hexdigest()


def generate_ascii_art(hash_string: str):
    """Создает ASCII-графику из части хеша."""
    banner = pyfiglet.figlet_format(hash_string[:12])
    print(banner)


def generate_qr_code(data: str, output_file: str = None):
    """Создает QR-код из строки и сохраняет, если указано имя файла."""
    qr = qrcode.QRCode(box_size=2, border=2)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    if output_file:
        img.save(output_file)
        print(f"[✓] QR сохранён в {output_file}")
    else:
        img.show()


def main():
    parser = argparse.ArgumentParser(description="Создает визуальный отпечаток криптовалютного адреса или транзакции.")
    parser.add_argument("input", help="Адрес или хеш транзакции")
    parser.add_argument("--qr", help="Сохранить QR-код в файл", metavar="файл.png")
    parser.add_argument("--algo", help="Алгоритм хеширования (по умолчанию sha256)", default="sha256")

    args = parser.parse_args()
    hash_str = hash_data(args.input, algo=args.algo)

    print(f"\n[+] Визуальный отпечаток (алгоритм: {args.algo}):")
    generate_ascii_art(hash_str)

    print(f"\n[+] Хеш: {hash_str}")

    if args.qr:
        generate_qr_code(args.input, args.qr)
    else:
        generate_qr_code(args.input)


if __name__ == "__main__":
    main()
