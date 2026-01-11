def min_pts(limit):
   def check(pts):
      if pts >= limit:
         return True
      return False
   return check

print("=== MIN 50 PTS TO PASS ===")
assess_test = min_pts(50)
print(assess_test)
print(f"52 pts -> {assess_test(52)}")
print(f"39 pts -> {assess_test(39)}")