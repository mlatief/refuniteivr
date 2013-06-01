from flask import Flask

app = Flask('refuniteivr')
app.config.from_object('refunite.ivrapp.settings')

import ivrcommon