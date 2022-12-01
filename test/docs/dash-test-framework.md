
# **DASH Testing Framework**

Here we describe a DASH testing framework that can be utilized for two main purposes:
1. To run highly scaled testing scenarios for SAI DASH testing
2. To write API agnostic tests to allow same script to run on multiple supported target APIs

## **Overview**

This testing framework was needed to mainly address the challenge of writing scaled tests to determine the limits of physical and virtual SAI implementations. SAI-challenger was used as the base framework. Below are some of the salient features of this current framework.

1. Support DPU as a target
2. DUT API abstraction 
3. Support of Thrift API in SAI Challenger
4. Multiple test config format
5. Support of SAI config gen format
6. Thrift agent refactoring to support all types of SAI object
7. More efficient way to convert SAI types
8. Added snappi way for flow definitions (packets formats, incremented fields)

## **High-level Diagram**

![High-level Diagram](../../images/confgen-hld-diag-ref.svg)

The generators produce Python data structures which can be rendered into output text (e.g. JSON) or used to feed custom applications such as a saithrift API driver, to directly configure a device. Likewise a custom API driver can be developed for vendor-specific APIs.

## **Detailed Diagram**

The following diagram reproduces the detailed inner structure of saigen and shows how a testcase can utilize the generator as imported Python modules to turbo-charge test-cases.

![Detailed Diagram](../../images/confgen-saichallenger-keys.svg)


## **Test Setup Details**

[Manual Setup](https://github.com/PLVision/DASH/blob/test-framework-extension/test/docs/dash-test-sai-challenger.md)

[Scale Format Description](https://github.com/PLVision/DASH/blob/test-framework-extension/test/test-cases/scale/saic/README.md)

[Helper files for testing](https://github.com/PLVision/DASH/blob/test-framework-extension/test/test-cases/scale/saic/dash_helper/vnet2vnet_helper.py)

[JSON files for snappi](https://github.com/PLVision/DASH/blob/test-framework-extension/test/test-cases/scale/saic/sai_dpu_client_server_snappi.json)

[JSON files for PTF](https://github.com/PLVision/DASH/blob/test-framework-extension/test/test-cases/scale/saic/sai_dpu_client_server_ptf.json)

[Test location](https://github.com/PLVision/DASH/tree/test-framework-extension/test/test-cases/scale/saic)

[Testbed Setup](https://github.com/PLVision/DASH/blob/test-framework-extension/dash-pipeline/README.md)

[SAI client abstraction](https://github.com/opencomputeproject/SAI-Challenger/tree/multi-api-support/common/sai_client/)

[SAI Clients](https://github.com/opencomputeproject/SAI-Challenger/blob/multi-api-support/docs/sai_clients.md)

[Dataplane Configuration](https://github.com/opencomputeproject/SAI-Challenger/blob/multi-api-support/docs/sai_dataplane.md)