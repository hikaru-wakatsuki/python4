def ft_crisis_response(text: str) -> None:
    try:
        with open(text) as f:
            print(f"ROUTINE ACCESS: Attempting access to '{text}'...")
            try:
                print(f"SUCCESS: Archive recovered - ``{f.read()}''")
            except Exception:
                print(f"CRISIS ALERT: Attempting access to '{text}'...")
                print("RESPONSE: Unexpected system anomaly "
                      "during data extraction")
                print("STATUS: Crisis handled, system stable")
                return
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{text}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
        return
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{text}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
        return
    except Exception:
        print(f"CRISIS ALERT: Attempting access to '{text}'...")
        print("RESPONSE: Unknown critical system anomaly")
        print("STATUS: Crisis handled, system stable")
        return


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print()
    ft_crisis_response("lost_archive.txt")
    print()
    ft_crisis_response("classified_vault.txt")
    print()
    ft_crisis_response("standard_archive.txt")
    print()
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
