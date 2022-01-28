from leavestracker.settings.base import *


DEBUG = True

SITE_URL = "localhost:8000"

# DATABASES = {
#             "default": {
#                         "ENGINE": DB_ENGINE,
#                                 "NAME": DB_NAME,
#                                         "USER": "myuser",
#                                                 "PASSWORD": "Sandwich1313",
#                                                         "HOST": "localhost",
#                                                                 "PORT": "5432",
#                                                                     },
#                 "readonly": {
#                             "ENGINE": DB_ENGINE,
#                                     "NAME": DB_NAME,
#                                             "USER": "myuser",
#                                                     "PASSWORD": "Sandwich1313",
#                                                             "HOST": "localhost",
#                                                                     "PORT": "5432",
#                                                                         }
#                 }

DATABASES = {
            "default": {
                        "ENGINE": DB_ENGINE,
                                "NAME": "d4qht1tndjqro7",
                                        "USER": "byerynhvowpzik",
                                                "PASSWORD": "24f330a0c7552adf67eedb0a3db93b896e627acd1885850ba6924262c64dad46",
                                                        "HOST": "ec2-184-73-243-101.compute-1.amazonaws.com",
                                                                "PORT": "5432",
                                                                    },
                "readonly": {
                            "ENGINE": DB_ENGINE,
                                    "NAME": "d4qht1tndjqro7",
                                            "USER": "byerynhvowpzik",
                                                    "PASSWORD": "24f330a0c7552adf67eedb0a3db93b896e627acd1885850ba6924262c64dad46",
                                                            "HOST": "ec2-184-73-243-101.compute-1.amazonaws.com",
                                                                    "PORT": "5432",
                                                                        }
                }
