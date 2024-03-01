import utils
import locale
import email_utils
from loguru import logger
from config import settings
from datetime import datetime
from shopping_list import shopping_list

locale.setlocale(locale.LC_ALL, "nb_NO.UTF-8")

plain = utils.render_plaintext(shopping_list)
html = utils.render_template(shopping_list)

logger.info("Generating shopping_list.html")

with open("Shopping_list.html", "w", encoding="utf8") as f:
    f.write(html)

logger.info("Sending emails")
email_utils.send_email(
    subject=f"Middags Planlegger {datetime.today()}", plain=plain, html=html
)

logger.info("Done!")
