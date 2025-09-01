# ColdEmailGenerator

A Python-based tool for generating personalized cold emails at scale. Designed to help professionals and businesses automate outreach while maintaining a personal touch, ColdEmailGenerator leverages customizable templates and user data to craft compelling messages.

## Features

- **Template-driven email generation**: Easily create and manage your own email templates.
- **Personalization**: Insert recipient-specific details for higher engagement.
- **Bulk processing**: Generate hundreds or thousands of emails in one go.
- **Export options**: Save generated emails to CSV, TXT, or other formats.
- **Easy configuration**: Set sender details, subject lines, and message bodies.
- **Extensible**: Add new personalization fields and templates as needed.

## Getting Started

### Prerequisites

- Python 3.7+
- (Optional) [pipenv](https://pipenv.pypa.io/en/latest/) or [virtualenv](https://virtualenv.pypa.io/)

### Installation

Clone the repository:

```bash
git clone https://github.com/US7103/ColdEmailGenerator.git
cd ColdEmailGenerator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Usage

1. Prepare your recipient data (CSV, JSON, etc.).
2. Create or edit your email templates in the `templates/` directory.
3. Run the generator script:

```bash
python generate_emails.py --recipients data/recipients.csv --template templates/default.txt --output output/emails.csv
```

For detailed options:

```bash
python generate_emails.py --help
```

### Example Template (`templates/default.txt`)

```
Subject: {{subject}}

Hi {{first_name}},

I noticed your work at {{company}} and thought you'd be interested in {{offer}}.

Best,
{{sender_name}}
```

### Output

Generated emails will be according to the specified format and its easy to copy.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change or add.

## License

This project is licensed under the MIT License.

## Contact

For questions or support, please open an issue on this repository or contact [US7103](https://github.com/US7103).
