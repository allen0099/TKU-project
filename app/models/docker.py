from app import db


class Docker(db.Model):
    __tablename__: str = "docker"

    id: int = db.Column(
        db.Integer,
        autoincrement=True,
        primary_key=True
    )
    practice_id: int = db.Column(
        db.Integer,
        db.ForeignKey("practice.id")
    )
    desc: str = db.Column(
        db.Text,
        nullable=False
    )
    url: str = db.Column(
        db.Text,
        nullable=False
    )
    port: int = db.Column(
        db.Integer,
        nullable=False
    )
    image: str = db.Column(
        db.Text
    )

    def __init__(
            self,
            belong: int,
            desc: str,
            url: str,
            port: int,
            image: str
    ) -> None:
        self.belong = belong
        self.desc = desc  # 題目描述
        self.url = url
        self.port = port
        self.image = image

    def __repr__(self) -> str:
        return f"<Docker {self.id}>"
