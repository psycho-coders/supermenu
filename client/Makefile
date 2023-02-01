.PHONY: clean
clean:
	$(eval IMAGES := $(shell docker images | grep 'client_supermenu' | awk '{ print $$3 }'))
	docker rmi $(IMAGES) --force 2>/dev/null; true

.PHONY: env
env:
	docker build -f ./Dockerfile -t client_supermenu:latest .
	docker run -it -p 8080:8080 --rm --name client_supermenu client_supermenu

%:
	@:
