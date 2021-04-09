from locust import task, User, TaskSet

from kafka_client import KafkaClient


class KafkaLocustUser(User):
    abstract = True

    def __init__(self, *args, **kwargs):
        super(KafkaLocustUser, self).__init__(*args, **kwargs)
        if not KafkaLocustUser.client:
            KafkaLocustUser.client = KafkaClient(KAFKA_BROKERS)


KAFKA_BROKERS = ['localhost:9092']


class KafkaBehavior(TaskSet):
    @task(100)
    def task1(self):
        self.client.send("test-topic",
                         message="{'key':'6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b','value':'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'}")


class KafkaUser(KafkaLocustUser):
    min_wait = 1
    max_wait = 1000
    tasks = [KafkaBehavior]
