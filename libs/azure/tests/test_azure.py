"""Test thredds dowazure-to-tar "https://geoau.blob.core.windows.net" "ey-gsa" "sv=2019-10-10&si=ey-gsa-ro&sr=c&sig=4T2mncGZ2v%2FqVsjjyHp%2Fv7BZytih8b251pSW0QelT98%3D" "baseline" "odc-metadata.yaml" --outfile ls78.tar.gz

azure-to-tar "https://geoau.blob.core.windows.net" "ey-gsa" "sv=2019-10-10&si=ey-gsa-ro&sr=c&sig=4T2mncGZ2v%2FqVsjjyHp%2Fv7BZytih8b251pSW0QelT98%3D" "L2/sentinel-2-nbar/" "ARD-METADATA.yaml" --outfile s2ab.tar.gz

azure-to-tar "https://geoau.blob.core.windows.net" "ey-gsa" "sv=2019-10-10&si=ey-gsa-ro&sr=c&sig=4T2mncGZ2v%2FqVsjjyHp%2Fv7BZytih8b251pSW0QelT98%3D" "linescan/" "odc-dataset.json" --outfile linescan.tar.gznloader code
"""
from odc.azure import find_blobs, download_yamls
import os
import pytest

@pytest.mark.xfail
def test_find_blobs():
    """Find blobs in a sample Azure account, this will fail if the blob store changes or is removed
    """

    account_name = "geoau"
    account_url = "https://" + account_name + ".blob.core.windows.net"
    container_name = "ey-gsa"
    credential = os.environ.get('AZURE_STORAGE_SAS_TOKEN')
    suffix = "odc-metadata.yaml"
    prefix = "baseline/ga_ls7e_ard_3/092/087/2018/05/25"

    blob_names = find_blobs(account_url, container_name, credential, prefix, suffix)
    assert blob_names
    assert len(list(blob_names)) == 1

@pytest.mark.xfail
def test_download_yamls():
    """Test pass/fail arms of YAML download from Azure blobstore
    """

    account_name = "geoau"
    account_url = "https://" + account_name + ".blob.core.windows.net"
    container_name = "ey-gsa"
    credential = os.environ.get('AZURE_STORAGE_SAS_TOKEN')

    test_blob_names = [
        "baseline/ga_ls7e_ard_3/092/087/2018/05/25/ga_ls7e_ard_3-0-0_092087_2018-05-25_final.odc-metadata.yaml"
    ]
    results = download_yamls(account_url, container_name, credential, test_blob_names)
    assert results
    assert len(list(results)) == 1
    assert results[0][0] is not None

