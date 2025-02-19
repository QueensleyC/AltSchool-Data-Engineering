from datetime import datetime, timezone
import uuid

class Expense:

    def __init__(self, title:str, amount:float):
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

    
    def update(self, title: str = None, amount = None):

        if title is not None:
            self.title = title

        if amount is not None:
            self.amount = amount

        self.updated_at = datetime.now(timezone.utc)

        
    def to_dict(self):
        return{
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
        
    def __str__(self):
        return f"Expense(title='{self.title}', amount={self.amount})"