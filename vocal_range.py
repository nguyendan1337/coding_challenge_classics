"""
PayPal Karat Interview - Vocal Range Problem

A singer has a vocal range defined by a lowest note and a highest note.
You are given a list of notes in a song.
Determine if the singer can perform the entire song, i.e., every note in the song
falls within the singer's vocal range (inclusive).

Note Representation:
- Notes are strings like "C4", "A5", "B3", "F4", "G5", etc.
- Pitches in ascending order: C < D < E < F < G < A < B
- Higher octave number means higher pitch.
- If octaves are the same, the later pitch letter is higher.

You need to implement two functions:
1. note_to_value(note: str) -> int
2. can_sing(low: str, high: str, song: list[str]) -> bool

"""

def note_to_value(note: str) -> int:
    """
    Convert a note like "C4" or "A5" to a single integer value for easy comparison.

    Hint: Map pitch letters to numbers (C=0, D=1, ..., B=6),
          then combine with octave: value = octave * 7 + pitch_value
    """
    pitch = note[0]
    pitch_value = 0
    octave = int(note[1])
    if pitch == "C":
        pitch_value = 0
    if pitch == "D":
        pitch_value = 1
    if pitch == "E":
        pitch_value = 2
    if pitch == "F":
        pitch_value = 3
    if pitch == "G":
        pitch_value = 4
    if pitch == "A":
        pitch_value = 5
    if pitch == "B":
        pitch_value = 6

    return octave * 7 + pitch_value



def can_sing(low: str, high: str, song: list[str]) -> bool:
    """
    Returns True if the singer can sing every note in the song,
    i.e., every note is between low and high (inclusive).

    You should use the note_to_value() helper function.
    """
    if not low and not high:
        return False
    if not song:
        return True
    lowest = note_to_value(low)
    highest = note_to_value(high)
    for note in song:
        song_note = note_to_value(note)
        if song_note < lowest or song_note > highest:
            return False

    return True

# ====================== Test Cases ======================
def run_tests():
    print("Running Vocal Range Tests...\n")

    test_cases = [
        # (low, high, song, expected)
        ("F4", "C5", ["C4", "G4", "B4", "C5"], False),
        ("F4", "C5", ["E4", "G4", "B4"], False),      # E4 is below F4
        ("F4", "C5", ["C4", "G4", "D5"], False),      # D5 is above C5
        ("A3", "D4", ["B3", "C4"], True),
        ("C4", "C5", [], True),                       # Empty song
        ("C4", "C4", ["C4"], True),                   # Single note at boundary
        ("B4", "D5", ["C5", "B4"], True),
        ("G4", "G4", ["G4"], True),
        ("C5", "C5", ["B4"], False),
    ]

    passed = 0
    for i, (low, high, song, expected) in enumerate(test_cases, 1):
        result = can_sing(low, high, song)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"Test {i}: low={low}, high={high}, song={song}")
        print(f"   Expected: {expected}, Got: {result} → {status}\n")
        if result == expected:
            passed += 1

    print(f"Summary: {passed}/{len(test_cases)} tests passed")


if __name__ == "__main__":
    run_tests()