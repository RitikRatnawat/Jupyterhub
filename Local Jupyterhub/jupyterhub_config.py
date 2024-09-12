# Configuration file for jupyterhub.
import os

c = get_config()  #noqa
c.Authenticator.allowed_users = {"test_user"}