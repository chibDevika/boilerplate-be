from leavestracker.settings.base import *

DEBUG = True

SITE_URL = "localhost:8000"

DATABASES = {
            "default": {
                        "ENGINE": DB_ENGINE,
                                "NAME": DB_NAME,
                                        "USER": "myuser",
                                                "PASSWORD": "Sandwich1313",
                                                        "HOST": "localhost",
                                                                "PORT": "5432",
                                                                    },
                "readonly": {
                            "ENGINE": DB_ENGINE,
                                    "NAME": DB_NAME,
                                            "USER": "myuser",
                                                    "PASSWORD": "Sandwich1313",
                                                            "HOST": "localhost",
                                                                    "PORT": "5432",
                                                                        }
                }
