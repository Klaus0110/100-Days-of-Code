def FirstNonRepeating(A):
		list = []
		mp = {}
		ans = ''

		for ch in A:
			if ch not in mp: 
				list.append(ch)
				mp[ch] = 1
			else:
				if ch in list:
					list.remove(ch)
			ans += list[0] if list else '#'

		return ans
l = "helloworldworldhello"
ans1 = FirstNonRepeating(l)
print(ans1)
