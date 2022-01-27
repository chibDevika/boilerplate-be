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
                                "NAME": "d546mov0jsogdj",
                                        "USER": "qtrcsrbixkupjb",
                                                "PASSWORD": "49bc45924ba1dfd760bb6369d40b749fb452a2bf93ca7fb9c8df1c65d612038f",
                                                        "HOST": "ec2-34-193-235-32.compute-1.amazonaws.com",
                                                                "PORT": "5432",
                                                                    },
                "readonly": {
                            "ENGINE": DB_ENGINE,
                                    "NAME": "d546mov0jsogdj",
                                            "USER": "qtrcsrbixkupjb",
                                                    "PASSWORD": "49bc45924ba1dfd760bb6369d40b749fb452a2bf93ca7fb9c8df1c65d612038f",
                                                            "HOST": "ec2-34-193-235-32.compute-1.amazonaws.com",
                                                                    "PORT": "5432",
                                                                        }
                }
