class ConfirmationHelper:
    def __init__(self, app):
        self.accept_next_alert = True
        self.app = app

    def assertRegexpMatches(self, param, param1):
        self.param = param
        self.param1 = param1

    def close_alert_and_get_its_text(self):
        wd = self.app.wd
        try:
            alert = wd.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            pass