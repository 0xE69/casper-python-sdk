
def test_that_a_transfer_can_be_encoded_as_json(LIB, FACTORY, deploy_params_static, vector_deploy_1):
    for vector in [v for v in vector_deploy_1 if v["typeof"] == "transfer"]:
        entity = FACTORY.create_deploy(
            deploy_params_static,
            FACTORY.create_standard_payment(
                vector["payment"]["amount"]
            ),
            FACTORY.create_standard_transfer_session(
                vector["session"]["amount"],
                vector["session"]["target"],
                vector["session"]["transfer_id"]
            )
        )
        as_json = LIB.serialisation.to_json(entity)
        # TODO: assert against a known JSON file
        assert isinstance(as_json, str)