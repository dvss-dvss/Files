WOWELS = ''

with open('Virsh.txt', encoding='UTF-8') as file:
    words = []
    for line in file:
        words += line.split()

starts_with_wowels_count = sum(
    1 for word in words
    if word[0].lower() in WOWELS
)

print('Слів, що починаються на голосну - ', starts_with_wowels_count)
print('Слів, що починаються на приголосну - ', len(words) - starts_with_wowels_count)