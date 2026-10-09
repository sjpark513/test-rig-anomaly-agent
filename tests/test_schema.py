from test_rig_agent.schema import AlarmRecord, Severity


def test_alarm_record_from_json():
    record = AlarmRecord.model_validate(
        {
            "occurred_at": "2026-10-12T09:15:00",
            "equipment": "Durability Rig 2",
            "alarm_code": "E-203",
            "severity": "warning",
            "probable_cause": "Load cell signal drift",
        }
    )
    assert record.severity is Severity.WARNING
    assert record.alarm_code == "E-203"
