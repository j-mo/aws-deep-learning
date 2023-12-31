from sagemaker.estimator import Framework


class AutoGluon(Framework):
    def __init__(
        self,
        entry_point,
        source_dir=None,
        hyperparameters=None,
        py_version="py3",
        framework_version=None,
        image_uri=None,
        distributions=None,
        **kwargs
    ):
        self.framework_version = framework_version
        self.py_version = py_version
        self.image_uri = image_uri
        super().__init__(
            entry_point,
            source_dir,
            hyperparameters,
            framework_version=framework_version,
            image_uri=self.image_uri,
            **kwargs,
        )
        super().__init__(entry_point, source_dir, hyperparameters, image_uri=image_uri, **kwargs)

    def _configure_distribution(self, distributions):
        return

    def create_model(
        self,
        model_server_workers=None,
        role=None,
        vpc_config_override=None,
        entry_point=None,
        source_dir=None,
        dependencies=None,
        image_name=None,
        **kwargs
    ):
        return None
