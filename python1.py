
q = []
s = input()
f = True
for i in range(len(s)):
  if s[i]=='(':
    q.append(s[i])
  if s[i]=='{':
    q.append(s[i])
  if s[i]=='[':
    q.append(s[i])
  if s[i]==')':
    if (q.pop()!='('):
      f = False
  if s[i]=='}':
    if (q.pop()!='{'):
      f=False
  if s[i]==']':
    if (q.pop()!='['):
      f=False

if len(q)==0 and f==True:
  f=True
else: f=False
print(f)

