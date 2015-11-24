from reportlab.pdfgen import canvas
import reportlab.rl_config


if __name__ == '__main__':
    reportlab.rl_config.warnOnMissingFontGlyphs = 0
    c = canvas.Canvas("./hello1.pdf",)
    c.drawString(100, 100, "Hello, world!")
    c.showPage()
    c.save()
