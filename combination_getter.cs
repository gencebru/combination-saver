
static void Main(string[] args)
{

    GetCombination(new List<int> { 
a,
b,
c,
d,
e,
f,
g,
h,
i,
j,
k,
l,
m,
n,
o,
p,
r,
s,
t,
u,
v,
w,
x,
y,
z  });
}

static void GetCombination(List<int> list)
{
    double count = Math.Pow(2, list.Count);
    for (int i = 1; i <= count - 1; i++)
    {
        string str = Convert.ToString(i, 2).PadLeft(list.Count, '0');
        for (int j = 0; j < str.Length; j++)
        {
            if (str[j] == '1')
            {
                Console.Write(list[j]);
            }
        }
        Console.WriteLine();
    }
}