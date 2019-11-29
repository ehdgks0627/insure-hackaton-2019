class Base:
    def __init__(self, data):
        self.birth_year = data.get('birth')
        self.height = data.get('height')
        self.weight = data.get('weight')
        self.is_male = data.get('gender') == '남성'
        self.job_category = data.get('job')
        self.smoke = data.get('smoke')  # 하루에 피는 담배 개비
        self.drink = data.get('drink')
