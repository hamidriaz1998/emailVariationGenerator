import re


def is_valid_email(email):
    """Validate the email address format."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


def generate_dot_variations(username):
    """Generate all possible dot variations for the username."""
    if not username:
        return []

    # Get all possible positions for dots (between characters)
    positions = len(username) - 1
    variations = set()

    # Generate all combinations of dot placements
    for i in range(2**positions):
        variation = list(username)
        offset = 0
        for pos in range(positions):
            if (i >> pos) & 1:
                variation.insert(pos + 1 + offset, ".")
                offset += 1
        variation = "".join(variation)
        # Only add valid variations (no consecutive dots, no leading/trailing dots)
        if ".." not in variation and variation[0] != "." and variation[-1] != ".":
            variations.add(variation)

    return variations


def generate_plus_variations(username, keywords=None):
    """Generate +something variations for the username."""
    if not keywords:
        keywords = ["netflix", "amazon", "signup", "test", "shop"]
    return [f"{username}+{keyword}" for keyword in keywords]


def generate_hyphen_underscore_variations(username):
    """Generate hyphen and underscore variations (provider-dependent)."""
    variations = set()
    variations.add(username.replace(".", "-"))  # Replace dots with hyphens
    variations.add(username.replace(".", "_"))  # Replace dots with underscores
    return variations


def generate_email_variations(
    email, include_hyphen_underscore=False, custom_keywords=None
):
    """Generate all possible email variations."""
    if not is_valid_email(email):
        return ["Invalid email format"]

    # Split email into username and domain
    username, domain = email.split("@")

    # Initialize variations list
    variations = set()

    # Add original email
    variations.add(email)

    # Generate dot variations (Gmail-compatible)
    dot_variations = generate_dot_variations(username)
    for dot_var in dot_variations:
        variations.add(f"{dot_var}@{domain}")

    # Generate +something variations
    plus_variations = generate_plus_variations(username, custom_keywords)
    for plus_var in plus_variations:
        variations.add(f"{plus_var}@{domain}")

    # Generate hyphen/underscore variations (optional)
    if include_hyphen_underscore:
        hyphen_underscore_variations = generate_hyphen_underscore_variations(username)
        for var in hyphen_underscore_variations:
            variations.add(f"{var}@{domain}")

    return sorted(list(variations))


def save_variations_to_file(variations, filename="email_variations.txt"):
    """Save the variations to a file."""
    with open(filename, "w", encoding="utf-8") as f:
        for variation in variations:
            f.write(variation + "\n")
    return filename


def main():
    # Get user input
    email = input("Enter your email address: ").strip()
    include_hyphen_underscore = (
        input("Include hyphen/underscore variations? (y/n): ").strip().lower() == "y"
    )
    custom_keywords_input = input(
        "Enter custom keywords for + variations (comma-separated, or press Enter for defaults): "
    ).strip()

    # Parse custom keywords
    custom_keywords = (
        [k.strip() for k in custom_keywords_input.split(",")]
        if custom_keywords_input
        else None
    )

    # Generate variations
    variations = generate_email_variations(
        email, include_hyphen_underscore, custom_keywords
    )

    # Print variations
    print("\nGenerated email variations:")
    for variation in variations:
        print(variation)

    # Save to file
    filename = save_variations_to_file(variations)
    print(f"\nVariations saved to {filename}")


if __name__ == "__main__":
    main()
