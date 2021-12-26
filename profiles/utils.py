import os

def resume_update_path(instance, filename):
    return os.path.join("resumes",
                        "profile_{}".format(instance.profile.id),
                        filename)