from typing import TextIO


def ft_archive_creation() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print()
    print("Initializing new storage unit: new_discovery.txt")
    text: str = "new_discovery.txt"
    try:
        f: TextIO = open(text, "w")
    except Exception as e:
        print(e)
        return
    print("Storage unit created successfully...")
    print()
    line1: str = "[ENTRY 001] New quantum algorithm discovered"
    line2: str = "[ENTRY 002] Efficiency increased by 347%"
    line3: str = "[ENTRY 003] Archived by Data Archivist trainee"
    print("Inscribing preservation data...")
    try:
        f.write(line1 + "\n")
        print(line1)
        f.write(line2 + "\n")
        print(line2)
        f.write(line3 + "\n")
        print(line3)
    except Exception as e:
        print(e)
        return
    finally:
        f.close()
    print()
    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{text}' ready for long-term preservation.")


if __name__ == "__main__":
    ft_archive_creation()
