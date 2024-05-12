from utils import get_date, masked, sorted_operations_status, sorted_operation_date, mask_account,mask_card_number, message_conversion
import pytest


def test_get_date():
    assert get_date("2019-07-13T18:51:29.313309") == "13.07.2019"
    assert get_date("2018-12-22T02:02:49.564873") == "22.12.2018"
    assert get_date("2019-08-19T16:30:41.967497") == "19.08.2019"


def test_masked():
    assert masked("Счет 71687416928274675290") == "Счет **5290"
    assert masked("Visa Gold 8326537236216459") == "Visa Gold 8326 53** **** 6459"
    assert masked("МИР 3766446452238784") == "МИР 3766 44** **** 8784"
    assert masked("MasterCard 6783917276771847") == "MasterCard 6783 91** **** 1847"
    assert masked("Maestro 1308795367077170") == "Maestro 1308 79** **** 7170"


def test_sorted_operations_status():
    assert (len(sorted_operations_status([{"state": "EXECUTED"}, {"state": "CANCELED"}])) == 1)


def test_sorted_operation_date():
    assert sorted_operation_date([{'date': "2018-06-12T07:17:01.311610"}, {'date': "2018-12-28T23:10:35.459698"}, {'date': "2018-02-22T00:40:19.984219"}])
    assert sorted_operation_date([{'date': "2019-01-15T17:58:27.064377"}, {'date': "2018-07-31T12:25:32.579413"}, {'date': "2019-04-11T23:10:21.514616"}])


def test_mask_account():
    assert mask_account("27804394774631586026") == "**6026"
    with pytest.raises(ValueError):
        assert mask_account("026")
    with pytest.raises(ValueError):
        assert mask_account("")

def test_mask_card_number():
    assert mask_card_number("6381702861749111") == "6381 70** **** 9111"
    with pytest.raises(ValueError):
        assert mask_card_number("63817061749111")
    with pytest.raises(ValueError):
        assert mask_card_number("")


def test_message_conversion():
    assert message_conversion([{
    "date": "2019-09-06T00:48:01.081967",
    "operationAmount": {
      "amount": "6357.56",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Gold 3654412434951162",
    "to": "Счет 59986621134048778289"
  }]) == "06.09.2019 Перевод организации "
         "Visa Gold 3654 41** **** 1162 -> Счет **8289)"
         "6357.56 USD"




