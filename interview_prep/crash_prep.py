from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# Create document
file_path = "/mnt/data/python_django_trading_cheatsheet.pdf"
doc = SimpleDocTemplate(file_path, pagesize=A4)
styles = getSampleStyleSheet()
elements = []

# Title
elements.append(Paragraph("<b>Python + Django + Trading Basics Cheat Sheet</b>", styles['Title']))
elements.append(Spacer(1, 12))

# Python Section
elements.append(Paragraph("<b>🐍 Python Basics</b>", styles['Heading2']))
python_points = [
    "Data Structures: list, dict, set, tuple.",
    "Comprehensions: [x for x in items], {k:v for k,v in dict}.",
    "OOP: class, __init__, __str__, inheritance.",
    "Error Handling: try/except, raise.",
    "Useful Modules: datetime, json, requests, logging."
]
for point in python_points:
    elements.append(Paragraph("• " + point, styles['Normal']))

elements.append(Spacer(1, 12))

# Django Section
elements.append(Paragraph("<b>🌐 Django Essentials</b>", styles['Heading2']))
django_points = [
    "Models: ForeignKey, ManyToMany, OneToOne.",
    "ORM: filter(), exclude(), select_related(), prefetch_related().",
    "Transactions: transaction.atomic(), select_for_update().",
    "DRF: APIView, ModelViewSet, Serializers.",
    "Auth: Django auth, JWT/Token auth.",
    "Async: Celery + Redis for background tasks."
]
for point in django_points:
    elements.append(Paragraph("• " + point, styles['Normal']))

elements.append(Spacer(1, 12))

# Databases Section
elements.append(Paragraph("<b>🗄 Databases & Systems</b>", styles['Heading2']))
db_points = [
    "SQL: SELECT, JOIN, INDEX, transactions.",
    "Redis: caching, queues.",
    "WebSockets: real-time price feeds (crypto).",
    "Deployment: env vars, settings split, gunicorn/uvicorn."
]
for point in db_points:
    elements.append(Paragraph("• " + point, styles['Normal']))

elements.append(Spacer(1, 12))

# Trading Basics Section
elements.append(Paragraph("<b>💹 Crypto Trading Basics</b>", styles['Heading2']))
trading_points = [
    "Order Types: market, limit, stop-loss.",
    "Latency: speed matters in execution.",
    "Exchanges: REST APIs (fetch data), WebSockets (live feeds).",
    "AI Use Cases: prediction, anomaly detection, backtesting."
]
for point in trading_points:
    elements.append(Paragraph("• " + point, styles['Normal']))

elements.append(Spacer(1, 12))

# Interview Tips
elements.append(Paragraph("<b>📝 Interview Quick Tips</b>", styles['Heading2']))
tips_points = [
    "Explain your thought process clearly.",
    "Use examples from your projects.",
    "Be curious: ask about data pipelines, deployment, testing.",
    "Stay calm on tricky questions – show learning ability."
]
for point in tips_points:
    elements.append(Paragraph("• " + point, styles['Normal']))

elements.append(Spacer(1, 12))

# Build PDF
doc.build(elements)
file_path
