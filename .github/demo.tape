# VHS tape recipe for crypto-service.github.io demo
# Render with: make demo or vhs .github/demo.tape

Output .github/demo.gif

Set Shell "zsh"
Set FontSize 14
Set Width 960
Set Height 600
Set Padding 20
Set Framerate 30
Set Theme "Catppuccin Mocha"
Set WindowBar Colorful
Set WindowBarSize 40
Set TypingSpeed 35ms

# Setup local alias and clean prompt
Hide
Type "export PS1='%F{cyan}crypto-service.github.io%f %F{yellow}❯%f '"
Enter
Type "clear"
Enter
Show

Sleep 600ms
Type "ssg --version"
Sleep 400ms
Enter
Sleep 1.2s

Type "make help"
Sleep 400ms
Enter
Sleep 1.5s

Type "make build"
Sleep 400ms
Enter
Sleep 3.5s

Type "ls -lh docs | head -n 12"
Sleep 400ms
Enter
Sleep 2.5s
