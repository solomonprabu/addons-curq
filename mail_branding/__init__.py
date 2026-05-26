from . import models
import base64
from odoo.tools.misc import file_path


def update_curqbot_name_in_res_users(env):
    curq_icon_base64 = base64.b64encode(
        open(file_path("mail_branding/static/img/curqbot.png"), "rb").read()
    ).decode("utf-8")
    root_user_id = env.ref("base.user_root", raise_if_not_found=False)
    if root_user_id:
        root_user_id.with_context(mail_notrack=True).write({"name": "CurqBot"})
        # Change image of root user
        root_user_id.with_context(mail_notrack=True).write(
            {"image_1920": curq_icon_base64}
        )


def uninstall_curqbot_name_in_res_users(env):
    """Uninstall hook for mail_branding module"""
    odoo_icon_base64 = base64.b64encode(
        open(file_path("mail/static/src/img/odoobot.png"), "rb").read()
    ).decode("utf-8")
    root_user_id = env.ref("base.user_root", raise_if_not_found=False)
    if root_user_id:
        root_user_id.with_context(mail_notrack=True).write({"name": "OdooBot"})
        root_user_id.with_context(mail_notrack=True).write(
            {"image_1920": odoo_icon_base64}
        )
