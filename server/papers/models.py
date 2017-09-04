from server.database import Model, db, Column, relationship


user_assoc = db.Table(
    'user_assoc',
    db.Column('user', db.Integer, db.ForeignKey('userprofile.id')),
    db.Column('paper', db.Integer, db.ForeignKey('papers.id'))
)

class Paper(Model):
    __tablename__ = 'papers'
    id = Column(db.Integer, primary_key=True)
    author = Column(db.Str, primary_key=True)
    title = Column(db.Str, nullable=True)
    subject = Column(db.Text, nullable=True)
    keywords = Column(db.String, nullable=True)
    pages = Column(db.Integer)
    # 文献的路径信息可以由文献的DOI号或者是文献标题获取到(判断有无)，文件的存放路径应该在配置文件中规定，不存到数据库，可以通过
    # property规范

    # user.profile.papers 获取到用户的所有信息
    owners = relationship(
        'UserProfile',
        secondary=user_assoc,
        # 个人文库，library
        backref='papers'
    )

    def __init__(self, author, title, subject, keyword):
        db.Model.__init__(cls, author=author, title=title)

    @property
    def name(self):
        if self.doi:
            return self.doi
        return self.title

    @property
    def pdf_path(self):
        return PDF_PATH.join(self.doi ? self.doi : self.title)

    @property
    def html_path(self):
        return HTML_PATH.join(...)

    @property
    def css_path(self):
        return CSS_PATH.join()
