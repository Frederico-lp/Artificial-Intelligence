import math

import matplotlib.pyplot as plt

import copy
import random
from math import exp

class Member:
    def __init__(self, name) -> None:
        self.name = name
        self.skills = []
        self.on_project = False
        self.working_on = -1

    def toString(self):
        string = self.name + " " + "\n"
        for i in range(len(self.skills)):
            string += self.skills[i].toString()

        return string

    def hasSkill(self, role):
        for skill in self.skills:
            if skill == role:
                return True

        return False


class Project:
    def __init__(self, name, duration, score, n_roles) -> None:
        self.name = name
        self.duration = duration
        self.score = score # score awarded for completing the project
        self.roles = [] # list of skills for contributors working on the project
        self.n_roles = n_roles
        self.has_started = False
        self.is_over = False

    def toString(self):
        string = self.name + " " + str(self.duration) + " " + str(self.score) + " " + str(self.n_roles) + "\n"
        for i in range(len(self.roles)):
            string += self.roles[i].toString()

        return string

    def check_requirements(self, team, num_project, member_is_chosen):
        assigned_members = []
        skills_matched = 0

        #If there are more roles than people, break
        if self.n_roles > len(member_is_chosen):
            return False

        #For each different role
        for i in range(self.n_roles):
            # For each member
            # When finding a member with the given skill, it breaks the for loop to prevent
            # looking for another member with the same skill
            k = 0
            for member in team.members:
                if member_is_chosen[k] and member.hasSkill(self.roles[i]) and not member.on_project:
                    skills_matched += 1
                    assigned_members.append(member)
                    #print("Has: " + member.toString())
                    break

                k += 1

        #print("Matched: ", skills_matched)
        #print("Needed skills: ", self.n_roles)
        #print("-----------------------------")

        #If all the requirements match start the project
        if skills_matched == self.n_roles:
            self.has_started = True
            # Assign the members to it
            for member in assigned_members:
                member.on_project = True
                member.working_on = num_project

            return True
        
        return False

class Team:
    def __init__(self, n_members, n_projects) -> None:
        self.n_members = n_members
        self.members = []
        self.n_projects = n_projects
        self.projects = []

    def toString(self):
        string = ""
        for i in range(self.n_members):
            string += self.members[i].toString()

        for i in range(self.n_projects):
            string += self.projects[i].toString()

        return string

class Skill:
    def __init__(self, name, level) -> None:
        self.name = name
        self.level = level

    def __eq__(self, other):
        return (self.name == other.name and self.level >= other.level)

    def toString(self):
        return self.name + " " + str(self.level) + "\n"

