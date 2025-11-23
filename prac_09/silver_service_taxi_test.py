from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test using assert statements."""
    taxi = SilverServiceTaxi("Hummer", 200, 2)
    taxi.drive(18)
    fare = taxi.get_fare()

    assert abs(fare - 48.80) < 0.01, f"Expected 48.78, got {fare}"

main()
