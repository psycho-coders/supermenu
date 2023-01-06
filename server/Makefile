.PHONY: local
local:
	python3 main.py

.PHONY: clean
clean:
	$(eval IMAGES := $(shell docker images | grep 'supermenu' | awk '{ print $$3 }'))
	docker compose -f dockerfiles/docker-compose.yml rm --stop --force -v
	docker rmi $(IMAGES) --force 2>/dev/null; true

.PHONY: docker
docker:
	docker compose -f dockerfiles/docker-compose.yml -p supermenu up

%:
	@:
