from enum import Enum


class MerchantDocumentStatus(Enum):
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    VERIFIED = "Verified"
    NOT_VERIFIED = "Not Verified"
