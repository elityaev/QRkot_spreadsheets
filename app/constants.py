from app.models import CharityProject, Donation

INV_DICT = {
    CharityProject: Donation,
    Donation: CharityProject
}
FORMAT = "%Y/%m/%d %H:%M:%S"