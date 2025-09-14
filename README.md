# 📧 Email Variations Generator Pro

A powerful and user-friendly tool for generating email address variations, perfect for testing, marketing, and email management purposes.

## ✨ Features

### 🎨 Modern GUI Interface

- **Engaging Design**: Beautiful gradient backgrounds, modern styling, and intuitive layout
- **Dark Mode Support**: Toggle between light and dark themes via the View menu
- **Animated Elements**: Hover effects, smooth transitions, and interactive buttons
- **Real-time Feedback**: Progress bars, status updates, and visual indicators
- **Professional Icons**: Emoji-enhanced interface for better user experience

### 🔧 Core Functionality

- **Dot Variations**: Generate all possible dot combinations (Gmail-compatible)
- **Plus Variations**: Create `+keyword` variations for email filtering
- **Custom Keywords**: Use your own keywords or default suggestions
- **Hyphen/Underscore**: Optional variations with alternative separators
- **Input Validation**: Real-time email format checking

### 💾 Enhanced Save Options

- **File Path Selection**: Browse and choose custom save locations
- **Default Fallback**: Automatic default filename if no path specified
- **Formatted Output**: Numbered lists with statistics in text files
- **Multiple Formats**: Support for various file extensions
- **Directory Creation**: Automatic creation of missing directories

### ⚡ Performance & UX

- **Threaded Processing**: Non-blocking generation with progress indicators
- **Smart Validation**: Enable/disable controls based on input state
- **Error Handling**: User-friendly error messages and recovery
- **Statistics Display**: Real-time count of generated variations

## 🚀 Quick Start

### Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd emailVariationGen
   ```

2. **Install dependencies**:
   ```bash
   pip install PyQt6
   ```

### Running the Application

#### GUI Version (Recommended)

```bash
python main.py
```

#### Command Line Version

```bash
python email_generator.py
```

## 📱 How to Use

### GUI Interface

1. **Enter Email Address**: Type your base email address
2. **Choose Theme**: Click the theme toggle button (🌙/☀️) in the top-right corner
3. **Configure Options**:
   - Check "Include hyphen/underscore variations" if needed
   - Add custom keywords for + variations (optional)
4. **Set Save Location**:
   - Use the browse button to select a file path
   - Or leave blank for default location
5. **Generate**: Click "Generate Variations" and watch the magic happen!
6. **Save**: Click "Save to File" to export your variations

### Example Usage

**Input**: `john.doe@gmail.com`

**Generated Variations**:

```
  1. john.doe@gmail.com
  2. johndoe@gmail.com
  3. jo.hn.doe@gmail.com
  4. john.d.oe@gmail.com
  5. john.doe+netflix@gmail.com
  6. john.doe+amazon@gmail.com
  7. john.doe+signup@gmail.com
  8. john.doe+test@gmail.com
  9. john.doe+shop@gmail.com
 10. john-doe@gmail.com (if hyphen option enabled)
 11. john_doe@gmail.com (if underscore option enabled)
```

## 🛠️ Technical Details

### Architecture

- **Frontend**: PyQt6 for modern, cross-platform GUI
- **Backend**: Pure Python with regex validation
- **Threading**: QThread for non-blocking operations
- **Styling**: CSS-like styling with gradients and animations

### File Structure

```
emailVariationGen/
├── main.py              # Enhanced GUI application (main entry point)
├── email_generator.py   # Core logic and CLI interface
├── README.md            # This file
└── pyproject.toml       # Dependencies and project configuration
```

### Dependencies

- Python 3.7+
- PyQt6

## 🎯 Use Cases

### Marketing & Testing

- **A/B Testing**: Create multiple email addresses for testing campaigns
- **Email Filters**: Use + variations to automatically sort emails
- **Account Management**: Organize different services with unique addresses

### Security & Privacy

- **Service Tracking**: Identify which services sell your email
- **Spam Prevention**: Use disposable variations for temporary signups
- **Organization**: Separate personal and professional communications

### Development & QA

- **Test Data**: Generate realistic email variations for testing
- **User Scenarios**: Simulate different user email patterns
- **Validation Testing**: Test email handling in applications

## 🔮 Advanced Features

### Custom Keywords

Add your own keywords for + variations:

- Work-related: `work`, `business`, `meetings`
- Shopping: `deals`, `coupons`, `orders`
- Social: `social`, `forums`, `newsletters`

### File Output Options

- **Text Files**: Formatted with numbers and statistics
- **CSV Format**: For spreadsheet import
- **Custom Paths**: Save anywhere on your system
- **Batch Processing**: Generate multiple sets efficiently

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Report Issues**: Found a bug? Let us know!
2. **Suggest Features**: Have an idea? We'd love to hear it!
3. **Submit PRs**: Code improvements are always welcome
4. **Documentation**: Help improve our docs

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

Having trouble? Check out these resources:

- **GitHub Issues**: Report bugs and request features
- **Documentation**: Comprehensive guides and examples
- **Community**: Connect with other users

## 🏆 Changelog

### Version 2.0 (Latest)

- ✨ Complete GUI redesign with modern styling
- 🌙 Dark mode support with theme switching
- 📁 File path selection with browse dialog
- ⚡ Threaded processing with progress indicators
- 📊 Real-time statistics and feedback
- 🎨 Enhanced visual design with animations
- 🔧 Improved error handling and validation
- 📂 Simplified file structure with main.py as entry point

### Version 1.0

- 📧 Basic email variation generation
- 💻 Command-line interface
- 📝 Simple file output

---

**Made with ❤️ for email power users**
