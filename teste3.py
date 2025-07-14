class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

l7 = ListNode(15)
l6 = ListNode(12, l7)
l5 = ListNode(11, l6)
l4 = ListNode(7, l5)
l3 = ListNode(4, l4)
l2 = ListNode(2, l3)
lista_1 = ListNode(1, l2)

_l9 = ListNode(21)
_l8 = ListNode(17, _l9)
_l7 = ListNode(13, _l8)
_l6 = ListNode(14, _l7)
_l5 = ListNode(9, _l6)
_l4 = ListNode(4, _l5)
_l3 = ListNode(3, _l4)
_l2 = ListNode(3, _l3)
lista_2 = ListNode(1, _l2)

def Solution(list1, list2):
    l1 = list1
    l2 = list2
    if (l1 is None or l1.val is None) and (l2 is None or l2.val is None):
        return None

    if l1 and l2:
        retorno = []
        while l1 and l2:
            if l1.val == l2.val:
                retorno.append(l1.val)
                retorno.append(l2.val)
                l1 = l1.next
                l2 = l2.next
                continue
            if l1.val < l2.val:
                retorno.append(l1.val)
                l1 = l1.next
            else:
                retorno.append(l2.val)
                l2 = l2.next
        if l1 is not None:
            while l1:
                retorno.append(l1.val)
                l1 = l1.next
        if l2 is not None:
            while l2:
                retorno.append(l2.val)
                l2 = l2.next
        list_node = ListNode(val=retorno[0])
        atual = list_node

        for v in retorno[1:]:
            atual.next = ListNode(v)
            atual = atual.next
        return list_node



Solution(lista_1, lista_2)
