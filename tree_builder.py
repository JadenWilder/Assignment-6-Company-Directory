
class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left subordinate.
        right (EmployeeNode): The right subordinate.
    '''

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None):
            Inserts an employee under the specified manager.
        print_tree(node=None, level=0):
            Prints the tree structure recursively.
    '''

    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        '''Insert an employee under a manager using recursion.'''

        if self.root is None:
            print("⚠️ Error: Add a team lead before adding employees.")
            return False

        side = side.strip().lower()

        if side not in ("left", "right"):
            print("❌ Invalid side. Enter LEFT or RIGHT.")
            return False

        if not manager_name.strip() or not employee_name.strip():
            print("❌ Manager name and employee name cannot be empty.")
            return False

        if current_node is None:
            current_node = self.root

        # Check whether the current node is the target manager.
        if current_node.name == manager_name:
            if side == "left":
                if current_node.left is not None:
                    print(
                        f"⚠️ {manager_name} already has "
                        "an employee on the LEFT."
                    )
                    return False

                current_node.left = EmployeeNode(employee_name)

            else:
                if current_node.right is not None:
                    print(
                        f"⚠️ {manager_name} already has "
                        "an employee on the RIGHT."
                    )
                    return False

                current_node.right = EmployeeNode(employee_name)

            print(
                f"✅ {employee_name} added to the "
                f"{side.upper()} of {manager_name}."
            )
            return True

        # Search the left subtree recursively.
        if current_node.left is not None:
            if self.insert(
                manager_name,
                employee_name,
                side,
                current_node.left
            ):
                return True

        # Search the right subtree recursively.
        if current_node.right is not None:
            if self.insert(
                manager_name,
                employee_name,
                side,
                current_node.right
            ):
                return True

        # Report a missing manager only after searching the tree.
        if current_node == self.root:
            print(f"❌ Manager '{manager_name}' was not found.")

        return False

    def print_tree(self, node=None, level=0):
        '''Print the company hierarchy using recursion.'''

        if node is None:
            if level == 0:
                node = self.root
                if node is None:
                    print("⚠️ The company directory is empty.")
                    return
            else:
                return

        print("  " * level + "- " + node.name)

        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)


# Test your code here


# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")

        choice = input("Choose an option (1–4): ").strip()

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ").strip()

                if not name:
                    print("❌ Employee name cannot be empty.")
                    continue

                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            if tree.root is None:
                print("⚠️ Add a team lead before adding employees.")
                continue

            manager = input("Enter the manager's name: ").strip()
            employee = input("Enter the new employee's name: ").strip()
            side = input(
                "Should this employee be on the LEFT or RIGHT "
                "of the manager? "
            ).strip()

            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳 Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break

        else:
            print("❌ Invalid option. Try again.")


if __name__ == "__main__":
    company_directory()
