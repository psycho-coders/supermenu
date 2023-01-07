.PHONY: local
local:
	PYTHONDONTWRITEBYTECODE=1 FIRESTORE_EMULATOR_HOST=localhost:8082 GOOGLE_APPLICATION_CREDENTIALS=./fake_creds.json python3 main.py

.PHONY: clean
clean:
	$(eval IMAGES := $(shell docker images | grep 'supermenu' | awk '{ print $$3 }'))
	docker compose -f dockerfiles/docker-compose.yml rm --stop --force -v
	docker rmi $(IMAGES) --force 2>/dev/null; true

.PHONY: env
env:
	docker compose -f dockerfiles/docker-compose.yml -p supermenu up -d

%:
	@:
