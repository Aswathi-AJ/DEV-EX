import matplotlib.pyplot as plt

a = [1, 2, 3, 4, 5]
b = [0, 0.6, 0.2, 15, 10]        # Shortened to match `a` length
c = [4, 2, 6, 8, 3]              # Must match length with `a`

plt.plot(a, b, 'or', label='b')  # Red circle markers
plt.plot(a, c, label='4th Rep')  # Default line for c

plt.xlabel('Day →')
plt.ylabel('Temp →')

ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_bounds(3, 40)

plt.xticks(list(range(1, 6)))
plt.yticks(list(range(0, 21, 5)))
plt.legend()
plt.title("Single Line Plot Example")
plt.grid(True)
plt.show()


import matplotlib.pyplot as plt

a = [1, 2, 3, 4, 5]
b = [0, 0.6, 0.2, 15, 10]
c = [4, 2, 6, 8, 3]
d = [8, 16, 21, 12, 7]  # Added for the 3rd subplot

fig = plt.figure(figsize=(10, 10))

sub1 = plt.subplot(2, 2, 1)
sub2 = plt.subplot(2, 2, 2)
sub3 = plt.subplot(2, 2, 3)
sub4 = plt.subplot(2, 2, 4)

sub1.plot(a, 'sb')  # Blue square markers
sub1.set_xticks(list(range(0, 10, 1)))
sub1.set_title('1st Rep')

sub2.plot(b, 'or')  # Red circle markers
sub2.set_xticks(list(range(0, 10, 2)))
sub2.set_title('2nd Rep')

sub3.plot([0, 3, 6, 9, 12], 'vg')  # Green triangle markers
sub3.set_xticks(list(range(0, 15, 3)))
sub3.set_title('3rd Rep')

sub4.plot(c, 'Dm')  # Magenta diamond markers
sub4.set_yticks(list(range(0, 24, 2)))
sub4.set_title('4th Rep')

plt.tight_layout()
plt.show()
