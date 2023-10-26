# oblig3_git_og_CI
- Jeg har kopiert filer fra oblig 2 og lagt de inn i oblig3_git_og_CI github repo
- Jeg har opprettet .github directory med workflows mappen inni,og deretter opprettet filen test.yml hvor jeg configurerer en workflow med navnet Test with Pytest

test.yml configurasjon:
"on:" definerer jeg når og hvor workflowen skal kjøre
 - på master branchen ved push- og pull-requests

"jobs:" Her definerer jeg hva og hvordan noe skal utføres
    - Den spesifikk oppgaven som skal utføres har jeg gitt navn "Run tests" som vises i github actions.
    - testene skal kjøres på siste versjon av ubuntu.

"steps:"
- Her definerer jeg hvilke steg jobben test skal utføre
- Først henter jeg innholdet fra repo til workflow
- Setter opp python versjonen som koden skal kjøre på
- Installerer avhengigheter med pip package manager fra filen requirements.txt (kjører kommandoen: pip install -r requirements.txt)
- Til sist kjøres testene fra test mappen med pytest test/
    