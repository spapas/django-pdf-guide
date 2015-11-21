# -*- coding: utf-8 -*-
from reportlab.pdfgen import canvas
import reportlab.rl_config
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


if __name__ == '__main__':
    c = canvas.Canvas("./hello2.pdf",)
    reportlab.rl_config.warnOnMissingFontGlyphs = 0
    pdfmetrics.registerFont(TTFont('DejaVuSans', 'DejaVuSans.ttf'))

    c.setFont('DejaVuSans', 22)
    c.drawString(100, 100, u"Καλημέρα ελλάδα.")

    c.showPage()
    c.save()
